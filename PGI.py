# Payment Gateway Interface

class PaymentGateway:
    def __init__(self, api_key, api_secret):
        """
        Initialize the payment gateway with API key and secret.

        :param api_key: API key for the payment gateway
        :param api_secret: API secret for the payment gateway
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def create_payment(self, amount, currency, payment_method):
        """
        Create a new payment request.

        :param amount: Amount to be paid
        :param currency: Currency of the payment
        :param payment_method: Payment method (e.g. credit card, PayPal)
        :return: Payment ID or error message
        """
        # Simulate a payment creation request
        payment_id = "PAY-123456789"
        return payment_id

    def get_payment_status(self, payment_id):
        """
        Get the status of a payment.

        :param payment_id: ID of the payment to check
        :return: Payment status (e.g. "paid", "pending", "failed")
        """
        # Simulate a payment status request
        payment_status = "paid"
        return payment_status

    def cancel_payment(self, payment_id):
        """
        Cancel a payment.

        :param payment_id: ID of the payment to cancel
        :return: Success or error message
        """
        # Simulate a payment cancellation request
        return "Payment cancelled successfully"

# Example usage
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    payment_gateway = PaymentGateway(api_key, api_secret)

    # Create a new payment
    amount = 10.99
    currency = "USD"
    payment_method = "credit_card"
    payment_id = payment_gateway.create_payment(amount, currency, payment_method)
    print("Payment ID:", payment_id)

    # Get the payment status
    payment_status = payment_gateway.get_payment_status(payment_id)
    print("Payment Status:", payment_status)

    # Cancel the payment
    cancellation_result = payment_gateway.cancel_payment(payment_id)
    print("Cancellation Result:", cancellation_result)
