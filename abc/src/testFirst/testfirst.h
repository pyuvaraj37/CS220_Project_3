/**CFile****************************************************************

  FileName    [testfirst.h]

  SystemName  [ABC: Logic synthesis and verification system.]

  PackageName []

  Synopsis    [External declarations.]

  Author      [Mariana Duarte]
  
  Affiliation [UC Riverside]

  Date        [Ver. 1.0. Started - May 14, 2021.]

  Revision    []

***********************************************************************/
 
#ifndef TESTFIRST_h
#define TESTFIRST_h


////////////////////////////////////////////////////////////////////////
///                          INCLUDES                                ///
////////////////////////////////////////////////////////////////////////
#include"base/main/main.h"

////////////////////////////////////////////////////////////////////////
///                         PARAMETERS                               ///
////////////////////////////////////////////////////////////////////////

ABC_NAMESPACE_HEADER_START


////////////////////////////////////////////////////////////////////////
///                         BASIC TYPES                              ///
////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
///                      MACRO DEFINITIONS                           ///
////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////
///                    FUNCTION DECLARATIONS                         ///
////////////////////////////////////////////////////////////////////////

/*=== testfirst.c ==========================================================*/
extern int TestFirst_FirstFunction(Abc_Frame_t * pAbc);
extern int TestFirst_FirstFunctionAbc(Abc_Frame_t * pAbc);

 

#endif

ABC_NAMESPACE_HEADER_END

////////////////////////////////////////////////////////////////////////
///                       END OF FILE                                ///
////////////////////////////////////////////////////////////////////////

