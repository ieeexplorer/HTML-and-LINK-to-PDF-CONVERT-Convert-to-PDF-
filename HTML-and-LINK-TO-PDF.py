import pdfkit
config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  
pdfkit.from_url("http://www.google.com", "google.pdf" , configuration = config)
pdfkit.from_file("test.html", "test.pdf" , configuration = config)
 