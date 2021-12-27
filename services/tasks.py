import csv
import os
from datetime import datetime
from random import randint

from faker import Faker

from accounts.models import CustomUser

faker = Faker()

POSSIBLE_KIND = {
    "Full Name": faker.name,
    "Job": faker.job,
    "Email": faker.email,
    "Domain name": faker.domain_name,
    "Phone number": faker.phone_number,
    "Company name": faker.company,
    "Text": faker.sentences,
    "Integer": randint,
    "Address": faker.address,
    "Date": faker.date,
}


@app.task
def generate_data(user_id, quantity):
    user = CustomUser.objects.get(pk=user_id)
    schemas = user.scheme.all()
    for scheme in schemas:
        scheme.set_processing()
        title = scheme.title
        columns = sorted(
            list(
                (
                    col.name,
                    col.kind,
                    col.order,
                    col.int_start,
                    col.int_end,
                    col.txt_sentences_quantity,
                )
                for col in scheme.column.all()
            ),
            key=lambda i: i[2],
        )
        if not columns:
            scheme.set_failed()
            return "Scheme has no columns"
        time_now = datetime.now().strftime("%Y%m%d%H%M%S%f")
        path_to_file = f"users_data/user_{user.uuid}/files/{title}_{time_now}.csv"
        os.makedirs(os.path.dirname("media/" + path_to_file), exist_ok=True)
        with open("media/" + path_to_file, mode="w+", newline="") as file:
            field_names = [col[0] for col in columns]
            writer = csv.DictWriter(
                file,
                fieldnames=field_names,
                delimiter=scheme.separator,
                quotechar=scheme.character,
            )
            writer.writeheader()

            for _ in range(int(quantity)):
                field_values = []

                for column in columns:
                    kind = column[1]
                    generator_function = POSSIBLE_KIND.get(kind)
                    if kind == "Text":
                        field_values.append(generator_function(column[5]))
                    elif kind == "Integer":
                        field_values.append(generator_function(column[3], column[4]))
                    else:
                        field_values.append(generator_function())

                writer.writerow(dict(zip(field_names, field_values)))

        scheme.file.name = path_to_file
        scheme.set_ready()
        scheme.save()
    return f"Success! Created rows: {quantity}"
