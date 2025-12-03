"""

           *
          * *
         *   *
        *     *
       *       *
      ***********
     * *       * *
    *   *     *   *
   *     *   *     *
  *       * *       *
 *         *         *
***********************

"""

a = int(input("Dime la altura: "))

for j in range(2):
    if j == 0:
        for i in range(a):
            if i == 0 or i == a-1:
                print(" "*(a-i+a) + "*"*(2*i+1))
            else:
                print(" "*(a-i+a) + "*" + " "*(2*i-1) + "*")
    else:
        for i in range(a):
            if i == a-1:
                print((" "*(a-i+1) + "*"*(2*i+1)) + (" "*(a-(2*i)+a-3) + "*"*(2*i)))
            elif i == 0:
                end=""
            else:
                print((" "*(a-i+1) + "*" + " "*(2*i-1) + "*") + (" "*(a-(2*i)+a-3) + "*" + " "*(2*i-1) + "*"))