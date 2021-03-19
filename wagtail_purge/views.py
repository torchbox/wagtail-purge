from django import forms
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from wagtail.admin import messages
from wagtail.contrib.frontend_cache.utils import purge_url_from_cache


class PurgePathForm(forms.Form):
    URL = forms.URLField(
        required=True,
        label=_("URL"),
        help_text=_(
            "Enter the full URL to purge, including trailing slash, if needed."
        ),
    )


def purge(request):
    if request.method == "POST":
        form = PurgePathForm(request.POST)
        if form.is_valid():
            URL = form.cleaned_data["URL"]
            purge_url_from_cache(URL)
            messages.success(request, _("Purge request submitted for %s") % URL)
            return redirect("purge")
    else:
        form = PurgePathForm()
    return render(
        request,
        "index.html",
        {
            "form": form,
        },
    )
