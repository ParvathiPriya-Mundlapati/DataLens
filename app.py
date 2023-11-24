from flask import Flask, render_template, request
import pandas as pd
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['datafile']
        if not f:
            return 'No file'

        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        df = pd.read_csv(stream)

        # Data quality checks
        missing_values = df.isnull().sum().to_frame('Missing Values')
        duplicates = df.duplicated().sum()
        stats = df.describe()

        return render_template('results.html', tables=[missing_values.to_html(classes='data'), stats.to_html(classes='data')], titles=missing_values.columns.values, duplicates=duplicates)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
