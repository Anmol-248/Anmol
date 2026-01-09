{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ac70b72-9fe8-462f-98a0-565b6bd51375",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/bin/bash\n",
    "# Start Flask backend and Streamlit dashboard (use two terminals ideally)\n",
    "export FLASK_APP=app.py\n",
    "flask run --host=0.0.0.0 --port=5000\n",
    "# In another terminal: streamlit run dashboard.py\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
