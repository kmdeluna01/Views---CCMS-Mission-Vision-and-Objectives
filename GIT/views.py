from django.http import HttpResponse

def mission(request):
    return HttpResponse("The College of Computer Studies shall produce technically competent Information Technology professionals adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.")
def vision(request):
    return HttpResponse("The College of Computer Studies shall be a Center of Excellence in Information Technology education.")
def obj(request):
    return HttpResponse("""<H1>CCS Program Educational Objectives</h1><h2>After graduation, alumni of MSEUF-CCS programs shall:</h2><h3>1. Be employedd and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions;</h3>
    <h3>2. Embark in lifelong learning or research to attune to the continuos innovation in the IT industry in order to adapt to the changing demands of the global market; and</h3>
    <h3>3. Exhibit leadership and teamwork,and commitment to their respective local or global organizations.</h3>""")

