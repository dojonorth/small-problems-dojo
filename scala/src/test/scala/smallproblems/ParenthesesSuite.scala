package smallproblems

import org.scalatest.FunSuite


class ParenthesesSuite extends FunSuite {
  import Main.parenthesesOne
  import Main.parenthesesTwo

  test("parentheses: empty string is valid") {
    assert(parenthesesOne(""))
    assert(parenthesesTwo(""))
  }

  test("parentheses: valid single set braces") {
    assert(parenthesesOne("()"))
    assert(parenthesesTwo("()"))
  }

  test("parentheses: invalid set brace") {
    assert(!parenthesesOne("("))
    assert(!parenthesesTwo("("))
  }

  test("parentheses: only closed brace") {
    assert(!parenthesesOne(")"))
    assert(!parenthesesTwo(")"))
  }

  test("parentheses: valid square braces") {
    assert(parenthesesOne("[]"))
    assert(parenthesesTwo("[]"))
  }

  test("parentheses: valid mixed braces") {
    assert(parenthesesOne("()[]{}"))
    assert(parenthesesTwo("()[]{}"))
  }

  test("parentheses: valid nested braces") {
    assert(parenthesesOne("({[]})"))
    assert(parenthesesTwo("({[]})"))
  }

  test("parentheses: some lisp") {
    assert(parenthesesOne("(sin (* 2 pi 1/4))"))
    assert(parenthesesTwo("(sin (* 2 pi 1/4))"))
  }

  test("parentheses: multiple nested groups") {
    assert(parenthesesOne("(+ (* 2 pi 1/4)(/ 8 (- 6 1)))"))
    assert(parenthesesTwo("(+ (* 2 pi 1/4)(/ 8 (- 6 1)))"))
  }

  test("parentheses: bad mixed") {
    assert(parenthesesOne("(+ (* 2 pi 1/4)(/ 8 (- 6 1)))"))
    assert(parenthesesTwo("(+ (* 2 pi 1/4)(/ 8 (- 6 1)))"))
  }

  test("parentheses: broken nested groups") {
    assert(!parenthesesOne("()([}))"))
    assert(!parenthesesTwo("()([}))"))
  }

}
