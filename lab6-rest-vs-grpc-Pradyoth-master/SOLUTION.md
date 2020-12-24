
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	        |---	        |-             --	|
|   REST add	|  2.48	        |2.7   	        |  215.06	        |
|   gRPC add	|0.508 	        | 0.474         |  108.52  	        |
|   REST img	|3.275          | 13.709        |  959.89 	        |
|   gRPC img	|5.834          | 13.754        |  142.67 	        |
|   PING        |0.038          | 0.408         |  107.742              |

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.

Note: All the above times are in milliseconds/query. 

gRPC outperforms REST when it comes to different regions Image API. It is almost 7 times faster than REST. It also outperforms REST when it comes to the add API and is almost twice as fast as REST when it comes to server and client in different regions. 


