# String comparisons - always consider case

When comparing strings, or checking if `substring x` is in `string y` - **always consider normalising the case of both strings!**

You might not want `Hello` to match `hello` - but you probably do. Either way, it should be a deliberate decision. Learned this one the hard way...
