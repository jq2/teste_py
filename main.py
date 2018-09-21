import module
import module_a
import module_b
import module_c

opts = {
        #id #function
        '0' : module.teste,
        '1' : module_a.teste,
        '2' : module_b.hello,
        '3' : module_c.scan
}

# Get the function ID
opt = str(input('Select an option: '))

# Call the module by passing the function ID
opts[opt]()




