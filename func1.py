from loanmetadata import data


def LoanProcess(CustName,Score,ReqAmt):
    if Score in range(50,400) and ReqAmt >=10000:
        print(f'Congratulations {CustName} you are approved for ${ReqAmt} You can also consider')
        for d in data:
            if Score in range(d['CS_Start']+1,d['CS_End']+1) and ReqAmt in range(d['Loan']+1):
                print(f''' ${d['Loan']} at {d['Interest']}% interest''')
    else:
        print('Your request is Denied')
