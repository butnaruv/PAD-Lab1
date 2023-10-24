using AutoMapper;
using Grpc.Core;
using TaskManagementService.Entites;
using TaskManagementService.Protos;
using TaskManagementService.Repositories;
using TaskManagerService = TaskManagementService.Protos.TaskManagerService;

namespace TaskManagementService.Services
{
    public class TaskService : TaskManagerService.TaskManagerServiceBase
    {
        private readonly ITaskRepository _taskManagerService;
        private readonly IMapper _mapper;

        public TaskService(ITaskRepository taskManagerService, IMapper mapper)
        {
            _taskManagerService = taskManagerService;
            _mapper = mapper;

        }
        public async override Task<Tasks> GetTaskListAsync(GetByEvent eventId, ServerCallContext context)
        {
            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                //await Task.Delay(6000);
                Console.WriteLine("GET ALL TASKS was called");
                var tasksDataTask = _taskManagerService.GetTaskListByEventIdAsync(eventId);
                await Task.WhenAny(tasksDataTask, Task.Delay(Timeout.Infinite, cts.Token));
                if (tasksDataTask.IsCompletedSuccessfully)
                {
                    var eventsData = tasksDataTask.Result;
                    Tasks response = new Tasks();
                    foreach (TaskModel dbTask in eventsData)
                    {
                        response.Items.Add(_mapper.Map<TaskDetails>(dbTask));
                    }
                    Console.WriteLine("Success!");
                    return response;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
            }

        }

        public async override Task<TaskDetails> GetTaskByIdAsync(GetByTaskId request, ServerCallContext context)
        {
            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                //await Task.Delay(5000);
                Console.WriteLine("GET TASK BY ID was called");
                var dbEventTask = _taskManagerService.GetTaskByIdAsync(request.TaskId);
                await Task.WhenAny(dbEventTask, Task.Delay(Timeout.Infinite, cts.Token));
                if (dbEventTask.IsCompletedSuccessfully)
                {
                    var dbTask = dbEventTask.Result;
                    var eventDetails = _mapper.Map<TaskDetails>(dbTask);
                    Console.WriteLine("Success!");
                    return eventDetails;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));

            }

        }

        public async override Task<TaskDetails> CreateTaskAsync(CreateNewTask request, ServerCallContext context)
        {
            Console.WriteLine("CREATE NEW TASK was called");

            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));
            try
            {
                var task = _mapper.Map<TaskModel>(request.Task);
                //await Task.Delay(1000);
                var createNewTaskTask = _taskManagerService.CreateTaskAsync(task);
                var test = await Task.WhenAny(createNewTaskTask, Task.Delay(Timeout.Infinite, cts.Token));

                if (createNewTaskTask.IsCompletedSuccessfully)
                {
                    var createNewTask = await _taskManagerService.CreateTaskAsync(task);
                    var taskDetails = _mapper.Map<TaskDetails>(task);
                    Console.WriteLine(taskDetails);
                    Console.WriteLine("Success!");
                    return taskDetails;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
            }
        }


        public async override Task<TaskDetails> UpdateTaskAsync(UpdateTask request, ServerCallContext context)
        {
            Console.WriteLine("UPDATE EVENT was called");
            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                var existingTaskTask = _taskManagerService.GetTaskByIdAsync(request.Task.Id);
                await Task.WhenAny(existingTaskTask, Task.Delay(Timeout.Infinite, cts.Token));
                if (existingTaskTask.IsCompletedSuccessfully)
                {
                    //var existingEvent = await _eventManagerService.GetEventByIdAsync(request.Event.Id);
                    var existingTask = existingTaskTask.Result;
                    if (request.Task.Status != "")
                    {
                        existingTask.Status = request.Task.Status;
                    }
                    if (request.Task.Name != "")
                    {
                        existingTask.Name = request.Task.Name;
                    }
                    if (request.Task.Deadline != "")
                    {
                        existingTask.Deadline = request.Task.Deadline;
                    }
                    if (request.Task.Description != "")
                    {
                        existingTask.Description = request.Task.Description;
                    }
                    var dbTask = _mapper.Map<TaskModel>(request.Task);

                    await _taskManagerService.UpdateTaskAsync(existingTask);

                    var eventDetails = _mapper.Map<TaskDetails>(existingTask);
                    Console.WriteLine("Success!");
                    return eventDetails;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
            }

        }

        public async override Task<DeleteTaskResponse> DeleteTaskAsync(DeleteTaskRequest request, ServerCallContext context)
        {
            Console.WriteLine("DELETE EVENT was called");
            var isDeleted = await _taskManagerService.DeleteTaskAsync(request.Id);
            var response = new DeleteTaskResponse
            {
                IsDeleted = isDeleted
            };
            Console.WriteLine("Success!");
            return response;
        }
    }
}
