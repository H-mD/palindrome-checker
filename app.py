from flask import Flask, render_template, request
from palindrome_checker import isPalindrome

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def palindrome_checker():
    result = None
    input_text = ""
    
    if request.method == 'POST':
        input_text = request.form.get('text', '')
        if input_text:
            is_palindrome = isPalindrome(input_text)
            if is_palindrome:
                result = f"PALINDROME"
            else:
                result = f"BUKAN PALINDROME"
        else:
            result = "INPUT KOSONG"
    
    return render_template('index.html', result=result, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)