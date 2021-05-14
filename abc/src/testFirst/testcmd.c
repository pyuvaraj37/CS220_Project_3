/**CFile****************************************************************

  FileName    [testcmd.c]

  SystemName  [ABC: Logic synthesis and verification system.]

  PackageName []

  Synopsis    []

  Author      [Mariana Duarte]
  
  Affiliation [UC Riverside]

  Date        [Ver. 1.0. Started - May 14, 2021.]

  Revision    []

***********************************************************************/

#include "base/main/main.h"
#include "testfirst.h"


ABC_NAMESPACE_IMPL_START

////////////////////////////////////////////////////////////////////////
///                        DECLARATIONS                              ///
////////////////////////////////////////////////////////////////////////
static int TestFirst_commandTestFirst(Abc_Frame_t * pAbc, int argc, char ** argv);

////////////////////////////////////////////////////////////////////////
///                     FUNCTION DEFINITIONS                         ///
////////////////////////////////////////////////////////////////////////

/**Function*************************************************************/
int TestFirst_commandTestFirst(Abc_Frame_t * pAbc, int argc, char ** argv){
    int fVerbose;
    int c, result;

    //set defaults
    fVerbose =0;
    //get arguments
    Extra_UtilGetoptReset();
    while ((c = Extra_UtilGetopt(argc, argv,"vh"))!= EOF){
        switch (c) {
        case 'v': fVerbose^= 1; break;
        case 'h': goto usage;
        default: goto usage;
        }
    }

    //call the main fucntion
    result = TestFirst_FirstFunctionAbc(pAbc);

    //print verbose information if the verbose mode is on
    if (fVerbose){
        Abc_Print(1,"\nVerbose mode is on.\n");
        if (result)
            Abc_Print(1,"The command finished successfully.\n");
        else
            Abc_Print(1,"The command execution has failled.\n");   
    }
    return 0;
usage:
    Abc_Print(-2, "usage: first cmd [-vh]\n");
    Abc_Print(-2, "\t First command in ABC. Print information about function read into ABC\n");
    Abc_Print(-2, "\t -v : verbose information, default [%s]\n", fVerbose ? "yes":"no");
    Abc_Print(-2, "\t -h : print the command usage\n");
    return 1;
}

void TestFirst_Init(Abc_Frame_t *pAbc){
    Cmd_CommandAdd(pAbc, "Various", "firstcmd",TestFirst_commandTestFirst,0);
}





//***********************************************************************/

////////////////////////////////////////////////////////////////////////
///                       END OF FILE                                ///
////////////////////////////////////////////////////////////////////////


ABC_NAMESPACE_IMPL_END