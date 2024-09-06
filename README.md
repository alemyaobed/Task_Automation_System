# Task Automation System

A comprehensive system for automating repetitive administrative tasks such as report generation and data backups. This project uses Python, Fabric, Celery, and PostgreSQL to streamline administrative workflows and integrate with external RESTful APIs.

## Features

- **Automated Tasks**: Generate reports and backup data automatically using Celery.
- **Task Scheduling**: Schedule tasks with Celery’s beat scheduler.
- **Fabric Integration**: Use Fabric to automate deployment and other administrative tasks.
- **API Integration**: Fetch data from external services using RESTful APIs.
- **Error Handling and Logging**: Implement robust error handling, logging, and alerting mechanisms.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Redis (for Celery)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/alemyaobed/Task_Automation_System.git
   cd Task_Automation_System
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Environment**

   Create a `.env` file in the root directory and add your environment variables. For example:

   ```plaintext
   DATABASE_URL=postgres://user:password@localhost:5432/task_automation
   CELERY_BROKER_URL=redis://localhost:6379/0
   CELERY_RESULT_BACKEND=redis://localhost:6379/0
   ```

5. **Set Up the Database**

   Ensure PostgreSQL is running and create the required tables. You can use a migration tool if needed.

   ```bash
   python manage.py migrate
   ```

6. **Start Celery**

   ```bash
   celery -A app.celery worker --loglevel=info
   ```

   And start Celery Beat for scheduling:

   ```bash
   celery -A app.celery beat --loglevel=info
   ```

7. **Run Fabric Tasks**

   To run Fabric tasks, use:

   ```bash
   fab generate_report
   fab backup_data
   ```

## Usage

- **Generate Reports**: Scheduled to run daily at midnight.
- **Backup Data**: Scheduled to run every Sunday at 1 AM.
- **API Integration**: Modify `app/api/services.py` to configure API requests.

## Testing

To run tests:

```bash
pytest
```

## Contributing

Feel free to fork the repository and submit pull requests. If you have any issues or feature requests, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Celery**: For task management and scheduling.
- **Fabric**: For task automation and deployment.
- **PostgreSQL**: For the database.
- **Redis**: For Celery’s message broker and result backend.

