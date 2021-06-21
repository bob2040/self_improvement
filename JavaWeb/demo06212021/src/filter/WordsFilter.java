<<<<<<< HEAD
package filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.List;

@WebFilter("/*")
public class WordsFilter implements Filter {

    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {

        ServletRequest proxy_req = (ServletRequest) Proxy.newProxyInstance(req.getClass().getClassLoader(), req.getClass().getInterfaces(), new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                if(method.getName().equals("getParameter")){
                    String value = (String) method.invoke(req, args);
                    req.setAttribute("original_text",value);
                    for (String str : words_list) {
                        if(value.contains(str)){
                            value = value.replaceAll(str,"***");
                        }
                    }
                    return value;
                }
                return method.invoke(req,args);
            }
        });
        chain.doFilter(proxy_req, resp);
    }

    private List<String> words_list = new ArrayList<String>();
        public void init(FilterConfig config) throws ServletException {
            try {
                ServletContext servletContext = config.getServletContext();
                String realPath = servletContext.getRealPath("/WEB-INF/classes/words.txt");
                BufferedReader br = new BufferedReader(new FileReader(realPath));
                String line = null;
                while((line = br.readLine()) != null){
                    words_list.add(line);
                }
                br.close();
                System.out.println(words_list);
            }catch (Exception e){
                e.printStackTrace();
            }
    }

    public void destroy() {
    }
}
=======
package filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.List;

@WebFilter("/*")
public class WordsFilter implements Filter {

    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {

        ServletRequest proxy_req = (ServletRequest) Proxy.newProxyInstance(req.getClass().getClassLoader(), req.getClass().getInterfaces(), new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                if(method.getName().equals("getParameter")){
                    String value = (String) method.invoke(req, args);
                    req.setAttribute("original_text",value);
                    for (String str : words_list) {
                        if(value.contains(str)){
                            value = value.replaceAll(str,"***");
                        }
                    }
                    return value;
                }
                return method.invoke(req,args);
            }
        });
        chain.doFilter(proxy_req, resp);
    }

    private List<String> words_list = new ArrayList<String>();
        public void init(FilterConfig config) throws ServletException {
            try {
                ServletContext servletContext = config.getServletContext();
                String realPath = servletContext.getRealPath("/WEB-INF/classes/words.txt");
                BufferedReader br = new BufferedReader(new FileReader(realPath));
                String line = null;
                while((line = br.readLine()) != null){
                    words_list.add(line);
                }
                br.close();
                System.out.println(words_list);
            }catch (Exception e){
                e.printStackTrace();
            }
    }

    public void destroy() {
    }
}
>>>>>>> 2ff42183102ce4aec61a17b46803747e5e656721
