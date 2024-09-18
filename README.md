# TimRedfin Project

## Description
TimRedfin is a Python project that interacts with the Redfin API to fetch neighborhood data. It includes functionalities to search for neighborhoods and gain insight into the market.

## Installation
1. Clone the repository:
    ```sh
    git clone # TODO update when uploaded
    cd # TODO
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Set up environment variables for Redfin credentials:
    ```sh
    export REDFIN_EMAIL=your_email
    export REDFIN_PWD=your_password
    ```

2. Run the Streamlit app:
    ```sh
    streamlit run main.py
    ```

3. Use the input field to search for a neighborhood and get the region ID.

## Testing
To run the tests, use the following command:
```sh
pytest
```