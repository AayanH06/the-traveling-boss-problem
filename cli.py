import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("square", type=int,
#                    help="display the square of a given number")
parser.add_argument("a", type=int, help="the base")
parser.add_argument("b", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
#answer = args.square**2
answer = args.a**args.b
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)