package smallproblems

import org.scalatest.FunSuite


class FactorialSuite extends FunSuite {
  import Main.factorialOne
  import Main.factorialTwo


  test("factorial: one") {
    assert(factorialOne(1) == 1)
    assert(factorialTwo(1) == 1)
  }

  test("factorial: four") {
    assert(factorialOne(4) == 24)
    assert(factorialTwo(4) == 24)
  }

  test("factorial: ten") {
    assert(factorialOne(10) == 3628800)
    assert(factorialTwo(10) == 3628800)
  }

}
