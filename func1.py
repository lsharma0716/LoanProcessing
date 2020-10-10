from loanmetadata import data

def LoanProcess(CustName,Score,ReqAmt):
    if Score in range(50,400) and ReqAmt >= 10000 and ReqAmt<=40000:
        print(f'Congratulations {CustName} you are approved for ${ReqAmt} You can also consider:')
        for criteria in data:
            if Score in range(criteria['CS_Start']+1,criteria['CS_End']+1) and ReqAmt in range(criteria['Loan']+1):
                print(f''' ${criteria['Loan']} at {criteria['Interest']}% interest for {criteria['Duration']} Months''')
    elif ReqAmt < 10000 or ReqAmt > 40000:
        print('Please enter amount in between $10000 to $40000')
    elif Score > 399:
        print('Your request is Denied. Credit Score out of range')
    else:
        print('Your request is Denied due to low credit score!')
