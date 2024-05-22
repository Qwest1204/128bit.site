from flask import Flask, render_template, request, redirect, flash, session
#from db.main_reg_fn import check_req, main_hash_fn, mainregfn, addlistarticle, listarticle, loginsql

application = Flask(__name__)



@application.route("/about/")
def Main_stranitsa():
    return render_template("main.html")
   

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    application.secret_key = 'GJHFKYKhgjkwueyfgjyTEUKFDRGlg65764%&%^TRFTYUERtTDFRTYDCnbWKHJG3'
    application.run(debug=True, port=4000, host="0.0.0.0")
