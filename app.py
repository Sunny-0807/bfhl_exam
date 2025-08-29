from flask import Flask, request, jsonify, Response
import json
from collections import OrderedDict

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route('/bfhl', methods=['POST'])
def bfhl_api():
    try:
        data = request.json.get('data')

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        
        for item in data:
            if item.isdigit():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_characters.append(item)
        
        alphabets_reversed = "".join(alphabets)[::-1]
        concat_string = ""
        for i, char in enumerate(alphabets_reversed):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
        
        response = OrderedDict([
            ("is_success", True),
            ("user_id", "hemakesh_surapureddy_08072005"),
            ("email", "hemakesh0807@gmail.com"),
            ("roll_number", "22BIT0288"),
            ("even_numbers", even_numbers),
            ("odd_numbers", odd_numbers),
            ("alphabets", alphabets),
            ("special_characters", special_characters),
            ("sum", str(total_sum)),
            ("concat_string", concat_string)
        ])
        
        return Response(json.dumps(response), mimetype='application/json'), 200        
    except Exception as e:
        error_response = {
            "is_success": False,
            "user_id": "your_full_name_ddmmyyyy",
            "email": "your_email@example.com",
            "roll_number": "your_roll_number",
            "error": str(e)
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(debug=True)