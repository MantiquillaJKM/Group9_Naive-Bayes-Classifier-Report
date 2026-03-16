# Hardcoded probabilities from table 
prior_yes = 8 / 13 
prior_no = 5 / 13 
 
# Conditional probabilities
cond_probs = { 
    "Weather": { 
        "sunny": {"yes": 3/8, "no": 1/5}, 
        "rainy": {"yes": 2/8, "no": 3/5}, 
        "cloudy": {"yes": 3/8, "no": 1/5} 
    }, 
    "TicketPrice": { 
        "cheap": {"yes": 4/8, "no": 1/5}, 
        "expensive": {"yes": 0/8, "no": 4/5}, 
        "medium": {"yes": 4/8, "no": 0/5} 
    }, 
    "Distance": { 
        "near": {"yes": 5/8, "no": 2/5}, 
        "far": {"yes": 3/8, "no": 3/5} 
    }, 
    "FriendsGoing": { 
        "true": {"yes": 5/8, "no": 1/5}, 
        "false": {"yes": 3/8, "no": 4/5} 
    } 
} 
 
# Get user input 
weather = input("Weather (sunny/rainy/cloudy): ").lower() 
ticket = input("Ticket price (cheap/medium/expensive): ").lower() 
distance = input("Distance to venue (near/far): ").lower() 
friends = input("Friends going (true/false): ").lower() 
 
# Compute probabilities 
prob_yes = ( 
    prior_yes * 
    cond_probs["Weather"][weather]["yes"] * 
    cond_probs["TicketPrice"][ticket]["yes"] * 
    cond_probs["Distance"][distance]["yes"] * 
    cond_probs["FriendsGoing"][friends]["yes"] 
) 
 
prob_no = ( 
    prior_no * 
    cond_probs["Weather"][weather]["no"] * 
    cond_probs["TicketPrice"][ticket]["no"] * 
    cond_probs["Distance"][distance]["no"] * 
    cond_probs["FriendsGoing"][friends]["no"] 
) 
 
# Normalize 
total = prob_yes + prob_no 
yes_percent = (prob_yes / total) * 100 
no_percent = (prob_no / total) * 100 
 
# Output 
print("\nProbability Results:") 
print(f"Attend Concert (YES): {yes_percent:.2f}%") 
print(f"Attend Concert (NO): {no_percent:.2f}%") 
 
if yes_percent > no_percent: 
    print("Prediction: You are more likely to ATTEND the concert.") 
else: 
    print("Prediction: You are more likely NOT to attend the concert.")