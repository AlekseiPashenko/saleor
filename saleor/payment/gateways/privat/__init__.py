import uuid

from ... import ChargeStatus, TransactionKind, CustomPaymentChoices
from ...interface import GatewayConfig, GatewayResponse, PaymentData
from .forms import PrivatPaymentForm

def privat_success():
    return True

def get_client_token(**_):
    """Generate a random client token."""
    return str(uuid.uuid4())

def create_form(data, payment_information, connection_params):
    return PrivatPaymentForm(data=data)      


def authorize(
        payment_information: PaymentData,
        config: GatewayConfig,
    ) -> GatewayResponse:
    
    success = privat_success()
    error = None

    if not success:
        error = "Unable to authorize transaction"
    # Handle connecting to the gateway and sending the auth request here
    # response = gateway.authorize(token=payment_information.token)

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=success,
        kind=TransactionKind.AUTH,
        amount=payment_information.amount,
        currency=payment_information.currency,
        transaction_id=payment_information.token,
        error=error,
    )  

def refund(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    error = None
    success = privat_success()
    if not success:
        error = "Unable to process capture"

    # Handle connecting to the gateway and sending the refund request here
    # response = gateway.refund(token=payment_information.token)

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=success,
        kind=TransactionKind.REFUND,
        amount=payment_information.amount,
        currency=payment_information.currency,
        transaction_id=payment_information.token,
        error=error,
    )


def capture(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Handle connecting to the gateway and sending the capture request here
    # response = gateway.capture(token=payment_information.token)
    error = None
    success = privat_success()
    if not success:
        error = "Unable to process capture"

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=success,
        kind=TransactionKind.CAPTURE,
        amount=payment_information.amount,
        currency=payment_information.currency,
        transaction_id=payment_information.token,
        error=error,
    )



def void(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Handle connecting to the gateway and sending the void request here
    # response = gateway.void(token=payment_information.token)
    error = None
    success = privat_success()
    if not success:
        error = "Unable to void the transaction."

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=success,
        kind=TransactionKind.VOID,
        amount=payment_information.amount,
        currency=payment_information.currency,
        transaction_id=payment_information.token,
        error=error,
    )



def process_payment(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    """Process the payment."""
    token = payment_information.token

    # Process payment normally if payment token is valid
    # if token not in dict(ChargeStatus.CHOICES):
    #     return capture(payment_information, config)

    # Process payment by charge status which is selected in the payment form
    # Note that is for testing by dummy gateway only
    charge_status = token
    authorize_response = authorize(payment_information, config)
    if charge_status == CustomPaymentChoices.MANUAL:
        return authorize_response

    if not config.auto_capture:
        return authorize_response

    # capture_response = capture(payment_information, config)
    # if charge_status == ChargeStatus.FULLY_REFUNDED:
    #     return refund(payment_information, config)
    # return capture_response
