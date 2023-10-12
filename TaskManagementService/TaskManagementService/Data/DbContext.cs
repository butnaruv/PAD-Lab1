using Microsoft.EntityFrameworkCore;
using System;
using TaskManagementService.Entites;

namespace TaskManagementService.Data
{
    public class DbContextClass : DbContext
    {
        protected readonly IConfiguration Configuration;

        public DbContextClass(IConfiguration configuration)
        {
            Configuration = configuration;
        }
        protected override void OnConfiguring(DbContextOptionsBuilder options)
        {
            options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection"));
        }

        public DbSet<TaskModel> Task { get; set; }
    }
}
