from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("admin/index.html")


@app.route('/viewUser')
def viewUser():
    return render_template("admin/viewUser.html")


@app.route('/addArea')
def addArea():
    return render_template("admin/addArea.html")


@app.route('/viewArea')
def viewArea():
    return render_template("admin/viewArea.html")


@app.route('/viewBranch')
def viewBranch():
    return render_template("admin/viewBranch.html")


@app.route('/viewVideos')
def viewVideos():
    return render_template("admin/viewVideos.html")


@app.route('/viewComplaints')
def viewComplaints():
    return render_template("admin/viewComplaints.html")


@app.route('/complaintReply')
def complaintReply():
    return render_template("admin/complaintReply.html")


@app.route('/viewFeedbacks')
def viewFeedbacks():
    return render_template("admin/viewFeedbacks.html")


if __name__ == '__main__':
    app.run(debug=True)
