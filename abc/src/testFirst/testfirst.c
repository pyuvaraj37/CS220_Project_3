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

ABC_NAMESPACE_IMPL_START

////////////////////////////////////////////////////////////////////////
///                        DECLARATIONS                              ///
////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
///                     FUNCTION DEFINITIONS                         ///
////////////////////////////////////////////////////////////////////////

/**Function*************************************************************/
int TestFirst_FirstFunction(Abc_Ntk_t * pNtk){
    //check if the network is strashed
    if(!Abc_NtkIsStrash(pNtk)){
        Abc_Print(-1, "TestFirst_FirstFunction: This command is only applicable to strashed networks \n");
        return 0;
    }
    //print Information about the network
    Abc_Print(1, "The network with name %s has:\n",Abc_NtkName(pNtk));
    Abc_Print(1, "\t - %d primary inputs \n",Abc_NtkPiNum(pNtk));
    Abc_Print(1, "\t - %d primary outputs \n",Abc_NtkPoNum(pNtk));
    Abc_Print(1, "\t - %d AND gates \n",Abc_NtkNodeNum(pNtk));

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

    return result;
}

//***********************************************************************/

////////////////////////////////////////////////////////////////////////
///                       END OF FILE                                ///
////////////////////////////////////////////////////////////////////////


ABC_NAMESPACE_IMPL_END