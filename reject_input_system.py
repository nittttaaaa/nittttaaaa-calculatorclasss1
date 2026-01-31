from flask import Flask, request, redirect, render_template_string
import csv
import os
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "reject_data.csv"

# bikin CSV + header kalau belum ada
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Date", "Process", "Problem Type",
            "Reject Qty", "Main Customer", "Workcenter"
        ])

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Reject Input System</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        input, select, button { padding: 6px; margin-right: 6px; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
        th { background: #f0f0f0; }
    </style>
</head>
<body>

<form method="post">
    <input type="date" name="date" required>
    
    <select name="process" required>
        <option value="">Process</option>
        <option>UV HOCK</option>
        <option>VARNISH</option>
        <option>LAMINATING</option>
        <option>WP GERMAN</option>
        <option>WP ESATEC</option>
        <option>WP ZHENGMAO 1</option>
        <option>WP ZHENGMAO 2</option>
        <option>FG MATTEL</option>
        <option>FG MASTER</option>
        <option>FG BICHENG</option>
        <option>FG BOBST</option>
        <option>JHOOK 1</option>
        <option>JHOOK 5</option>
        <option>LINE 1</option>
        <option>LINE 2</option>
        <option>LINE 3</option>
        <option>LINE 4</option>
        <option>PH 1</option>
        <option>PH 2</option>
        <option>PH 3</option>
        <option>PH 4</option>
        <option>PH 5</option>
        <option>PH 6</option>
        <option>PH 7</option>
        <option>PH 8</option>
        <option>PH 9</option>
        <option>PH 10</option>
        <option>PH 11</option>
        <option>PH 12</option>
        <option>PH 13</option>
        <option>PH 14</option>
        <option>PH 15</option>
        <option>PH 16</option>
        <option>PH 17</option>
        <option>PH 18</option>
        <option>PH 19</option>
        <option>PH 20</option>
        <option>PH 21</option>
        <option>PH 22</option>
        <option>HS 1</option>
        <option>HS 2</option>
        <option>HS 3</option>
        <option>HS 4</option>
        <option>HS 5</option>
        <option>HS 6</option>
        <option>SABLON SEMI AUTO</option>
        <option>LINE BORONGAN</option>
        <option>FG ROLAM</option>
        <option>VACUUM 1 (Cutting 1)</option>
        <option>VACUUM 2 (Cutting 4)</option>
        <option>VACUUM 3 (Cutting 6)</option>
        <option>VACUUM 4 (Cutting 7)</option>
    </select>

    <input type="text" name="problem" placeholder="Problem Type" required>
    <input type="number" name="qty" placeholder="Reject Qty" required>
    <input type="text" name="customer" placeholder="Main Customer" required>
    <input type="text" name="workcenter" placeholder="Workcenter" required>

    <button type="submit">Submit</button>
</form>

<table>
<tr>
    <th>Date</th><th>Process</th><th>Problem</th>
    <th>Qty</th><th>Customer</th><th>Workcenter</th>
</tr>
{% for row in data %}
<tr>
{% for col in row %}
<td>{{ col }}</td>
{% endfor %}
</tr>
{% endfor %}
</table>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        row = [
            request.form["date"],
            request.form["process"],
            request.form["problem"],
            request.form["qty"],
            request.form["customer"],
            request.form["workcenter"]
        ]

        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(row)

        return redirect("/")

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        data = list(csv.reader(f))[1:]

    return render_template_string(HTML, data=data)

if __name__ == "__main__":
    app.run(debug=True)



