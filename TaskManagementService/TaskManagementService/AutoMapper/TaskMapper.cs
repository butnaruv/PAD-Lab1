using AutoMapper;
using TaskManagementService.Entites;
using TaskManagementService.Protos;

namespace TaskManagementService.AutoMapper
{
    public class TaskMapper : Profile
    {
        public TaskMapper()
        {
            CreateMap<TaskModel, TaskDetails>().ReverseMap();
        }
    }
}
