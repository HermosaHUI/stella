#include "CodeGen.h"
#include "Parser.h"
#include "Sema.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Support/InitLLVM.h"
#include "llvm/Support/raw_ostream.h"
#include <istream>

static llvm::cl::opt<std::string>
  Input(llvm::cl::Positional,
        llvm::cl::desc('<input expression>'),
        llvm::cl::init(''));

int main(int argc, const char **argv) {
  return 0;
}
