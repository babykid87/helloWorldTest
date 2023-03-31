from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! from Tuan Nguyen! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

#@app.route('/favourite-course')
#def favourite():
 #   print ('Subject: ' + request.args.get('subject'))
  #  print('Subject: ' + request.args.get('subject'))
   # fun_courses = ['BMGT302','BMGT402']
   # return render_template('favourite-course.html', courses=fun_courses)
#add about routing
@app.route('/favourite-course')
def favourite():
    print ('You entered your favourite class as: ' + request.args.get('subject')+ request.args.get('course_number'))
    return render_template('favourite-course.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
