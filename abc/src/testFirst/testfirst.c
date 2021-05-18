/**CFile****************************************************************

  FileName    [testfirst.c]

  SystemName  [ABC: Logic synthesis and verification system.]

  PackageName []

  Synopsis    []

  Author      [Mariana Duarte]
  
  Affiliation [UC Riverside]

  Date        [Ver. 1.0. Started - May 14, 2021.]

  Revision    []

***********************************************************************/
#include"base/main/main.h"
#include "proof/fraig/fraig.h"

ABC_NAMESPACE_IMPL_START

////////////////////////////////////////////////////////////////////////
///                        DECLARATIONS                              ///
////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
///                     FUNCTION DEFINITIONS                         ///
////////////////////////////////////////////////////////////////////////

/**Function*************************************************************/
int TestFirst_FirstFunction(Abc_Ntk_t * pNtk){
    Abc_Print(1, "The network with name %s has:\n",Abc_NtkName(pNtk));
    Abc_Print(1, "\t - %d primary inputs \n",Abc_NtkPiNum(pNtk));
    Abc_Print(1, "\t - %d primary outputs \n",Abc_NtkPoNum(pNtk));
    Abc_Print(1, "\t - %d AND gates \n",Abc_NtkNodeNum(pNtk));
    //check if the network is strashed
    if(!Abc_NtkIsStrash(pNtk)){
        Abc_Print(-1, "TestFirst_FirstFunction: This command is only applicable to strashed networks \n");
        pNtk = Abc_NtkStrash(pNtk,1,0,0);
        Abc_Print(1, "Strash\n");
    }
    //print Information about the network
    Abc_Print(1, "The network with name %s has:\n",Abc_NtkName(pNtk));
    Abc_Print(1, "\t - %d primary inputs \n",Abc_NtkPiNum(pNtk));
    Abc_Print(1, "\t - %d primary outputs \n",Abc_NtkPoNum(pNtk));
    Abc_Print(1, "\t - %d AND gates \n",Abc_NtkNodeNum(pNtk));
    

    Fraig_Params_t Params, * pParams = &Params;
    memset( pParams, 0, sizeof(Fraig_Params_t) );
    pParams->nPatsRand  = 2048; // the number of words of random simulation info
    pParams->nPatsDyna  = 2048; // the number of words of dynamic simulation info
    pParams->nBTLimit   =  100; // the max number of backtracks to perform
    pParams->fFuncRed   =    1; // performs only one level hashing
    pParams->fFeedBack  =    1; // enables solver feedback
    pParams->fDist1Pats =    1; // enables distance-1 patterns
    pParams->fDoSparse  =    1; // performs equiv tests for sparse functions
    pParams->fChoicing  =    1; // enables recording structural choices
    pParams->fTryProve  =    1; // tries to solve the final miter
    pParams->fVerbose   =    1; // the verbosiness flag
    pParams->fVerboseP  =    1; // the verbosiness flag

    Abc_Ntk_t * pAbchange;
    pAbchange = Abc_NtkFraig(pNtk,&Params,1,1);

    Abc_Print(1, "FRAIG  with name %s has:\n",Abc_NtkName(pAbchange));
    Abc_Print(1, "\t - %d primary inputs \n",Abc_NtkPiNum(pAbchange));
    Abc_Print(1, "\t - %d primary outputs \n",Abc_NtkPoNum(pAbchange));
    Abc_Print(1, "\t - %d AND gates \n",Abc_NtkNodeNum(pAbchange));

    return 1;
}
//***********************************************************************/


int TestFirst_FirstFunctionAbc(Abc_Frame_t * pAbc){
    Abc_Ntk_t * pNtk;
    int result;

    //get the network that is read into ABC
    pNtk = Abc_FrameReadNtk(pAbc);

    if (pNtk == NULL){
        Abc_Print(-1, "TestFirst_FirstFunctionAbc: getting the network has failed \n");
        return 0;
    }

    //call the main function
    result = TestFirst_FirstFunction(pNtk);
    //Abc_Ntk_t * pAbchange;

    //if (!Abc_NtkIsStrash(pNtk)){
    //pNtk = Abc_NtkStrash(pNtk,1,0,0);
    //} 

   // pAbchange = Abc_NtkToFraig(pAbchange,NULL,1,1);
    return result;
}

//***********************************************************************/

////////////////////////////////////////////////////////////////////////
///                       END OF FILE                                ///
////////////////////////////////////////////////////////////////////////


ABC_NAMESPACE_IMPL_END