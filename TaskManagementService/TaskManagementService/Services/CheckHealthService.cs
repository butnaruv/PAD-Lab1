using Grpc.Core;
using Microsoft.Data.SqlClient; 

namespace TaskManagementService.Services
{
    public class CheckHealthService : CheckHealth.CheckHealthBase
    {
        public override async Task<HealthResponse> CheckHealth(HealthRequest request, ServerCallContext context)
        {
            Console.WriteLine("Health was checked!");

            try
            {
                using (var connection = new SqlConnection("Data Source=DESKTOP-UQJOT1B;Initial Catalog=Tasks;Integrated Security=SSPI;Encrypt=False;"))
                {
                    await connection.OpenAsync();
                    if (connection.State == System.Data.ConnectionState.Open)
                    {
                        return new HealthResponse { HealthMeassage = "DatabaseConnectionServing" };
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Database connection error: {ex.Message}");
            }

            return new HealthResponse { HealthMeassage = "NotServing" };
        }
    }
}
