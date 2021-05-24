import csv
import logging

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from datetime import datetime

LOG = logging.getLogger(__name__)
logging.basicConfig(filename="database_logs.log", level=logging.INFO, format="%(asctime)s: %(message)s")

YEARS = ["2019", "2020"]


def write_last_row(year, line):
    open('LastRow.txt', 'w').close()  # clean previous data from file
    with open('LastRow.txt', "w") as file:
        file.write(f"{year}, {line // 10 * 10}")


def read_last_row():
    with open('LastRow.txt', "r") as file:
        try:
            year, row = file.read().split(",")
        except ValueError:
            year, row = "2019", 0
        row = int(row)
    return year, row


def insert_data_into_collections(line, year, general_coll: Collection, dicts_to_write, start_time):
    try:
        if (dicts_to_write):
            general_coll.insert_many(dicts_to_write)
            write_last_row(year, line)
    except Exception as e:
        end_time = datetime.now()
        LOG.info(f"Break time {end_time}")
        LOG.info(f"Executing time {end_time - start_time}")
        LOG.info(f"Fallen: {e}")
        raise e
    return 0


def insert_data(general_coll: Collection, csv_filename, year, last_row, start_time):
    previous_stack_time = start_time
    LOG.info(f"Inserting data from {last_row} row from file for {year} year")

    with open(csv_filename, encoding="cp1251") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        i = 0
        dicts_to_write = []
        for row in csv_reader:
            i += 1
            print(i)
            if i <= last_row:
                continue

            formatted_dict = clean_dict(row, year)
            dicts_to_write.append(formatted_dict)

            if i % 10 == 0:
                insert_data_into_collections(i, year, general_coll, dicts_to_write, start_time)
                dicts_to_write = []

    if i % 10 != 0:
        insert_data_into_collections(i, year, general_coll, dicts_to_write, start_time)

    LOG.info(f"Inserting from {csv_filename} is finished")


def clean_dict(dict_to_clean, year):
    dict_to_clean["TestYear"] = year
    for key in dict_to_clean:
        try:
            new_value = float(dict_to_clean[key].replace(",", "."))
            dict_to_clean[key] = new_value
        except Exception:
            pass
    return dict_to_clean


def get_query(general_coll: Collection):
    """Варіант №5. Порівняти середній бал з Історії України у кожному регіоні у 2020 та 2019 роках серед тих кому
    було зараховано тест"""
    LOG.info("Getting data for query")
    query = general_coll.aggregate(
        [
            {"$match": {"histTestStatus": "Зараховано"}},
            {"$group": {"_id": {"year": "$TestYear",
                                "region": "$REGNAME"},
                        "HistAverage": {"$avg": "$histBall100"}}},
        ]
    )

    with open("query.csv", "w") as csvfile:
        csq_writer = csv.DictWriter(csvfile, fieldnames=["year", "region", "HistAverage"])
        csq_writer.writeheader()
        for row in query:
            row["year"] = row["_id"]["year"]
            row["region"] = row["_id"]["region"]
            del row["_id"]
            csq_writer.writerow(row)
    LOG.info(f"Users query data recorded into query.csv")


def main():
    start_time = datetime.now()
    LOG.info(f"Start time {start_time}")

    client = MongoClient(port=27017)
    db = client.lab4

    general_coll = db.general
    # year, row = read_last_row()
    #
    # index = YEARS.index(year)
    # for year in YEARS[index:]:
    #     insert_data(general_coll, f"Odata{year}File.csv", year, row, start_time)
    #     row = 0
    #
    # end_time = datetime.now()
    # LOG.info(f"End time {end_time}")
    # LOG.info(f"Inserting executing time {end_time - start_time}")

    get_query(general_coll)

    client.close()

    LOG.info("Program is finished")


if __name__ == "__main__":
    main()

#  number of all rows in files = 733112
