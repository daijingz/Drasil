module Data.Drasil.Constraints where

import Language.Drasil

gtZeroConstr :: Constraint
gtZeroConstr = physc $ (:<) (Int 0)