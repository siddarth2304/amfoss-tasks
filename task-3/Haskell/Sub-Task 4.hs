main :: IO ()
main = do
    n <- readFile "input.txt"
    writeFile "output.txt" (unlines (diamond (read n :: Int)))

diamond :: Int -> [String]
diamond n = top ++ bottom
  where
    top = [replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- [0 .. n - 1]]
    bottom = reverse (init top)
