from py_cgnat.calculator.direct import cgnat_direct
from py_cgnat.calculator.reverse import cgnat_reverse
from py_cgnat.utils.parser import parser


# Main program run at terminal.
def main():
    args = parser.parse_args()
    kwargs = args._get_kwargs()
    keys = sorted(key for key, _ in kwargs)  
    try:
        if keys == ['module', 'private_net', 'public_net', 'source_addr']:
            # Using translator module
            if type(args.source_addr) == tuple: # using --reverse
                pass
            else: # using --direct
                pass
        else: # keys == ['module', 'output_file', 'private_net', 'public_net', 'target_platform']
            # Using generator module
            gen_call(args.output_file, args.private_net, args.public_net, args.target_platform)
    except BaseException as e:
        print(e)


# Call to run generator module.
def gen_call(output_file, private_net, public_net, target_platform):
    generate = __import__(f'py_cgnat.generator.{target_platform}', fromlist=['generate']).generate    
    rules = generate(private_net, public_net)
    if output_file:
        with open(output_file, 'w') as fp: fp.write(rules)
    else:
        print(rules, end='')


if __name__ == '__main__':
    main()
