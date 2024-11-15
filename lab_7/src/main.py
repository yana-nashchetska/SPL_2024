# src/main.py
import sys
import os

# sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "."))

from api_provider import ApiProvider
from data_repository import DataRepository
from unit_of_work import UnitOfWork
from user_interface import UserInterface
from data_parser import DataParser
from data_saver import DataSaver
from error_handler import ErrorHandler
from history_logger import HistoryLogger


def main():
    api_provider = ApiProvider()
    repository = DataRepository(api_provider)
    unit_of_work = UnitOfWork(repository)
    ui = UserInterface()
    parser = DataParser()
    saver = DataSaver()
    error_handler = ErrorHandler()
    logger = HistoryLogger()

    print("Welcome to the data management app!")

    while True:
        user_input = input("\nEnter command ('get posts', 'get users', 'exit'): ")

        # Використання парсера для команд користувача
        command = parser.parse_command(user_input)
        if command is None:
            print("Invalid command. Please try again.")
            continue

        try:
            if command == "exit":
                print("Exiting the program.")
                break
            elif command == "get posts":
                # Fetch and display posts data
                unit_of_work.load_data("posts")
                data = unit_of_work.commit()
                ui.display_table(data)

                # Log and save data
                logger.log_request(command, data)
                saver.save_as_json(data)  # Другий параметр - це ім'я файлу
                saver.save_as_csv(data)
            elif command == "get users":
                # Fetch and display users data
                unit_of_work.load_data("users")
                data = unit_of_work.commit()
                ui.display_table(data)

                # Log and save data
                logger.log_request(command, data)
                saver.save_as_json(data)
                saver.save_as_csv(data)
            else:
                print("Unknown command.")

        except Exception as e:
            error_handler.handle_error(e)


if __name__ == "__main__":
    main()
