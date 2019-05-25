import uuid

from ... import ChargeStatus, TransactionKind
from ...interface import GatewayConfig, GatewayResponse, PaymentData
from .forms import PrivatPaymentForm

def get_client_token(**_):
    """Generate a random client token."""
    return str(uuid.uuid4())


def authorize(
        payment_information: PaymentData,
        config: GatewayConfig,
    ) -> GatewayResponse:

    # Handle connecting to the gateway and sending the auth request here
    response = gateway.authorize(token=payment_information.token)

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=response.is_success,
        transaction_id=response.transaction.id,
        kind=TransactionKind.AUTH,
        amount=response.amount,
        currency=response.currency,
        error=get_error(response),
        raw_response=get_payment_gateway_response(response),
    )  

def refund(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Handle connecting to the gateway and sending the refund request here
    response = gateway.refund(token=payment_information.token)

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=response.is_success,
        transaction_id=response.transaction.id,
        kind=TransactionKind.REFUND,
        amount=response.amount,
        currency=response.currency,
        error=get_error(response),
        raw_response=get_payment_gateway_response(response),
    )


def capture(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Handle connecting to the gateway and sending the capture request here
    response = gateway.capture(token=payment_information.token)

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=response.is_success,
        transaction_id=response.transaction.id,
        kind=TransactionKind.CAPTURE,
        amount=response.amount,
        currency=response.currency,
        error=get_error(response),
        raw_response=get_payment_gateway_response(response),
    )



def void(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Handle connecting to the gateway and sending the void request here
    response = gateway.void(token=payment_information.token)

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=response.is_success,
        transaction_id=response.transaction.id,
        kind=TransactionKind.VOID,
        amount=response.amount,
        currency=response.currency,
        error=get_error(response),
        raw_response=get_payment_gateway_response(response),
    )



def charge(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Handle connecting to the gateway and sending the charge request here
    response = gateway.charge(
        token=payment_information.token,
        amount=payment_information.amount,
    )

    # Return a correct response format so Saleor can process it,
    # the response must be json serializable
    return GatewayResponse(
        is_success=response.is_success,
        transaction_id=response.transaction.id,
        kind=TransactionKind.CHARGE,
        amount=response.amount,
        currency=response.currency,
        error=get_error(response),
        raw_response=get_payment_gateway_response(response),
    )



def process_payment(
    payment_information: PaymentData,
    config: GatewayConfig,
) -> GatewayResponse:

    # Authorize, update the token, then capture
    authorize_response = authorize(payment_information, config)
    payment_information.token = authorize_response.transaction_id

    capture_response = capture(payment_information, config)

    return capture_response



def create_form(data, payment_information, connection_params):
    return PrivatPaymentForm(
        data,
        payment_information,
        connection_params,
    )    
