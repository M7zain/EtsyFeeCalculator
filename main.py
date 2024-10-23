def calculate_etsy_fees(listing_price):
    # Etsy fee constants
    listing_fee = 7  # TL
    transaction_fee_rate = 0.065  # 6.5% transaction fee
    processing_fee = 14  # TL
    processing_fee_rate = 0.065  # 6.5% processing fee (including State fee)
    regulatory_fee_rate = 0.0227  # 2.27% Regulatory Operating fee
    vat_fee = 55  # VAT ~55 TL
    state_fee_rate = 0.078  # ~7.80% State fee

    # Calculate individual fees
    transaction_fee = listing_price * transaction_fee_rate
    processing_fee_total = (listing_price * processing_fee_rate) + processing_fee 
    regulatory_fee = listing_price * regulatory_fee_rate
    state_fee = listing_price * state_fee_rate

    # Total Etsy fees
    total_fees = (
        listing_fee +
        transaction_fee +
        processing_fee_total +
        regulatory_fee +
        vat_fee
    )

    return total_fees


while True:
    # User input for the listing price, allows 'exit' to break the loop
    user_input = input("Enter your listing price in Turkish Lira (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
        listing_price = float(user_input)
        # Calculate total fees Etsy will cut
        total_etsy_fees = calculate_etsy_fees(listing_price)
        # Output the result
        print(f"Etsy will cut approximately {total_etsy_fees:.2f} TL from your listing price.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number for the listing price.\n")
