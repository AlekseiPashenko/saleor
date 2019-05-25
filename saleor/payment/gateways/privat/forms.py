from django import forms



class PrivatPaymentForm(forms.Form):
    amount = forms.DecimalField()
    payment_method_nonce = forms.CharField()

    def get_payment_token(self):
        return self.cleaned_data["payment_method_nonce"]


    