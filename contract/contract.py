from solc import compile_source
from contract.code import Code

class Contract:
    def compile():
        compiled_sol = compile_source(Code.source_code())
        contract_interface = compiled_sol['<stdin>:RandomContract']
        return contract_interface
    def compile_input(rawcode):
        compiled_sol = compile_source(rawcode)
        contract_interface = compiled_sol['<stdin>:RandomContract']
        return contract_interface
