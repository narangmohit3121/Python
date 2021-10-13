class Outer(object):

    def show_outer_message(self, msg):
        print("This is outer class")
        print(msg)

    class Inner(object):

        def show_inner_message(self, msg):
            print("This is inner class")
            print(msg)


outer = Outer()
inner = outer.Inner()

outer.show_outer_message("Message for outer object")
inner.show_inner_message("Message for inner object")