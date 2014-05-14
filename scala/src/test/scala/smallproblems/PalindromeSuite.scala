package smallproblems

import org.scalatest.FunSuite


class PalindromeSuite extends FunSuite {
  import Main.palindromeOne
  import Main.palindromeTwo


  test("palindrome: bob is true") {
    assert(palindromeOne("bob"))
    assert(palindromeTwo("bob"))
  }

  test("palindrome: bobo is false") {
    assert(!palindromeOne("bobo"))
    assert(!palindromeTwo("bobo"))
  }

  test("palindrome: Ignores case") {
    assert(palindromeOne("Bob"))
    assert(palindromeTwo("Bob"))
  }

  test("palindrome: Ignores punctuation") {
    assert(palindromeOne("A man, a plan, a canal: Panama"))
    assert(palindromeTwo("A man, a plan, a canal: Panama"))
  }
}
