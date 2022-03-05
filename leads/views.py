from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "name": "John",
        "age": 35,
        "leads": leads
    }
    # return HttpResponse("Hello world")
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):

    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead

    }
    return render(request, "leads/lead_detail.html", context)


def lead_create_view(request):
    form = LeadModelForm()
    if request.method == "POST":
        print("We are receiving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("Lead has been created")
            form = LeadModelForm()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update_view(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            print("form is updated")
            form = LeadModelForm()
            return redirect("/")
    context = {
        "form": form,
        "lead": lead
    }

    return render(request, "leads/lead_update.html", context)


def lead_delete_view(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/")

# def lead_update_view(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         print("We are receiving a post request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print("This form is valid")
#             print(form.cleaned_data)
#             age = form.cleaned_data['age']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']

#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             print("Lead has been created")
#             form = LeadForm()
#             return redirect("/")
#     context = {
#         "form": form,
#         "lead": lead

#     }
#     return render(request, "leads/lead_update.html", context)


# def lead_create_view(request):   Notice that we can further shorten this form by removinf all the validations as seen above
    # form = LeadForm()
    # if request.method == "POST":
    #     print("We are receiving a post request")
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         print("This form is valid")
    #         print(form.cleaned_data)
    #         age = form.cleaned_data['age']
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         agent = Agent.objects.first()
    #         Lead.objects.create(
    #             first_name=first_name, last_name=last_name, age=age, agent=agent
    #         )
    #         print("Lead has been created")
    #         form = LeadForm()
#             return redirect("/")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
