import re

def get_ai_response(message):
    # More detailed response mappings
    responses = {
        "hello": "Hello! How can I assist you with your yatra planning today? Feel free to ask me about our travel packages, insurance, or any other travel-related queries.",
        "hi": "Hi there! I'm here to help you with your yatra planning. What can I do for you today?",
        "hey": "Hey! How can I assist you with your yatra plans? You can ask me about travel packages, insurance details, or anything else you need.",
        "price": "For pricing details, kindly contact us at 9995553690. We offer various packages, and our team will provide you with all the necessary information.",
        "cost": "The cost of our travel packages varies depending on the destination and the package selected. Please reach out to us at 9995553690 for detailed pricing information.",
        "package": "We offer a variety of travel packages to suit your needs. You can find more details on our packages page or contact us for personalized recommendations.",
        "packages": "Our travel packages include options for different interests and budgets. Visit our packages page to explore the available options or contact us for more details.",
        "offers": "We have special offers and discounts on certain travel packages. Check our offers page or contact us to find out about the latest deals.",
        "insurance": "We provide comprehensive travel insurance that covers medical emergencies, trip cancellations, lost luggage, and more. Visit our insurance page for detailed coverage information.",
        "insurance coverage": "Our travel insurance covers a range of situations including medical emergencies, trip cancellations, lost luggage, and travel delays. For a detailed breakdown, please refer to our insurance page or contact us.",
        "medical coverage": "Our travel insurance includes medical coverage for emergency situations while you're traveling. This ensures that you get the necessary medical assistance if needed during your trip.",
        "trip cancellation": "Our insurance policy includes trip cancellation coverage, which reimburses you for non-refundable expenses if you have to cancel your trip due to unforeseen circumstances.",
        "lost luggage": "We offer coverage for lost or delayed luggage through our travel insurance. This helps you recover the cost of essential items if your luggage is delayed or lost during your journey.",
        "emergency assistance": "Our travel insurance includes 24/7 emergency assistance services to help you with medical emergencies, travel disruptions, and other urgent situations while you're abroad.",
        "travel packages": "Our travel packages range from basic options to luxury experiences. We offer customized packages based on your preferences and budget. Check out our packages page or get in touch for more details."
    }
    
    # Normalize message by lowering the case
    message = message.lower()
    
    # Check for keywords and phrases in the message
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', message):
        return responses["hello"]
    elif re.search(r'\bprice\b|\bcost\b', message):
        return responses["price"]
    elif re.search(r'\bpackage\b|\bpackages\b|\boffers\b', message):
        return responses["package"]
    elif re.search(r'\binsurance\b|\binsurance coverage\b|\bmedical coverage\b|\btrip cancellation\b|\blost luggage\b|\bemergency assistance\b', message):
        return responses["insurance"]
    elif re.search(r'\btravel packages\b', message):
        return responses["travel packages"]
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase? If you need help with travel packages, insurance, or pricing, just let me know!"

# Example usage
user_message = "Hi there, can you tell me more about travel insurance coverage?"
response = get_ai_response(user_message)
print(response)
