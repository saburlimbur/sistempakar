from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/diagnosa", methods=["GET", "POST"])
def diagnosa_page():
    hasil = None
    # deskripsi = None

    if request.method == 'POST':
        nama = request.form.get('nama')
        gejala = request.form.getlist('gejala')

        # 1. Semua gejala lengkap
        semua_gejala = ['demam', 'pilek', 'batuk', 'sakit_tenggorokan',
                        'nyeri_otot', 'sakit_kepala', 'kelelahan']
        if all(g in gejala for g in semua_gejala):
            hasil = f"Halo {nama}, kemungkinan Anda terkena <strong>flu berat atau COVID-19</strong>."

        # 2. Demam, pilek, dan batuk
        elif all(g in gejala for g in ['demam', 'pilek', 'batuk']):
            hasil = f"Halo {nama}, kemungkinan Anda terkena <strong>flu</strong>."

        # 3. Pilek dan sakit tenggorokan
        elif all(g in gejala for g in ['pilek', 'sakit_tenggorokan']):
            hasil = f"Halo {nama}, kemungkinan Anda mengalami <strong>radang tenggorokan ringan</strong>."

        # 4. Tidak ada demam, pilek, atau batuk
        elif not any(g in gejala for g in ['demam', 'pilek', 'batuk']):
            hasil = f"Halo {nama}, Anda <strong>tidak mengalami flu</strong>."

        # 5. Selain itu
        else:
            hasil = f"Halo {nama}, penyakit Anda <strong>belum dapat diindikasikan</strong> berdasarkan gejala yang dipilih."

    return render_template("diagnosa.html", hasil=hasil)


@app.route("/riwayat")
def riwayat_page():
    return render_template("riwayat.html")


@app.route("/informasi")
def informasi_page():
    return render_template("informasi.html")


if __name__ == "__main__":
    app.run(debug=True)
