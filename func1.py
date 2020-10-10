from loanmetadata import data


def LoanProcess(CustName,Score,ReqAmt):
    if Score in range(50,400) and ReqAmt >=10000:
        print(f'Congratulations {CustName} you are approved for ${ReqAmt} You can also consider:')
        for criteria in data:
            if Score in range(criteria['CS_Start']+1,criteria['CS_End']+1) and ReqAmt in range(criteria['Loan']+1):
                print(f''' ${criteria['Loan']} at {criteria['Interest']}% interest for {criteria['Duration']} Months''')
    else:
        print('Your request is Denied')
