#include <llvm/IR/LLVMContext.h>
#include <llvm/IR/Function.h>
#include <llvm/IR/Module.h>
#include <llvm/IRReader/IRReader.h>
#include <llvm/Support/SourceMgr.h>
#include <llvm/Support/CommandLine.h>

static llvm::ManagedStatic<llvm::LLVMContext> GlobalContext;
static llvm::cl::opt<std::string> InputFilename(llvm::cl::Positional, llvm::cl::desc("<filename>.bc"), llvm::cl::Required);

int main(int argc, char **argv) {
    llvm::SMDiagnostic Err;
    llvm::cl::ParseCommandLineOptions(argc, argv);
    std::unique_ptr<llvm::Module> M = llvm::parseIRFile(InputFilename, Err, *GlobalContext);
    if (!M) {
        Err.print(argv[0], llvm::errs());
        return 1;
    }
    for (llvm::Function &F : *M) {
        llvm::outs() << F.getName() << "\n";
    }
}
