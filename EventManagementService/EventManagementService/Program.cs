using EventManagementService.Data;
using EventManagementService.Repositories;
using EventManagementService.Services;
using Microsoft.Extensions.Diagnostics.HealthChecks;



var builder = WebApplication.CreateBuilder(args);

// Additional configuration is required to successfully run gRPC on macOS.
// For instructions on how to configure Kestrel and gRPC clients on macOS, visit https://go.microsoft.com/fwlink/?linkid=2099682

// Add services to the container.
builder.Services.AddGrpc();
builder.Services.AddScoped<IEventRepository, EventRepository>();
builder.Services.AddDbContext<DbContextClass>();
IServiceCollection serviceCollection = builder.Services.AddAutoMapper(typeof(Program).Assembly);

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<EventService>();
app.MapGrpcService<CheckHealthService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();

